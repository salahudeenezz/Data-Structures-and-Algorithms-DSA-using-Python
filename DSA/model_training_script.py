from transformers import MarianMTModel, MarianTokenizer, Trainer, TrainingArguments
from datasets import load_dataset, Dataset

try:
    # Load the tokenizer and model
    model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Load the prepared data
    train_data = Dataset.from_json('train_twi_text_data.json')
    val_data = Dataset.from_json('val_twi_text_data.json')

    # Preprocess the data
    def preprocess_function(examples):
        inputs = examples['Twi Text']
        targets = examples['English Translation']
        model_inputs = tokenizer(inputs, max_length=128, truncation=True)
        with tokenizer.as_target_tokenizer():
            labels = tokenizer(targets, max_length=128, truncation=True)
        model_inputs['labels'] = labels['input_ids']
        return model_inputs

    train_data = train_data.map(preprocess_function, batched=True)
    val_data = val_data.map(preprocess_function, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=val_data,
    )

    # Train the model
    trainer.train()

    # Save the model
    model.save_pretrained('./twi_translation_model')
    tokenizer.save_pretrained('./twi_translation_model')
    
    print("Model training completed successfully.")

except Exception as e:
    print(f"An error occurred during model training: {e}")
